{
  description = "Application packaged using poetry2nix";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable-small";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.flake-utils.follows = "flake-utils";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        myapp = { poetry2nix, lib }: poetry2nix.mkPoetryApplication {
          projectDir = self;
          overrides = poetry2nix.defaultPoetryOverrides.extend
            (final: prev: {
              advent-of-code-data = prev.advent-of-code-data.overridePythonAttrs
              (
                old: {
                  buildInputs = (old.buildInputs or [ ]) ++ [ prev.setuptools ];
                }
              );
            });        };
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            poetry2nix.overlays.default
            (final: _: {
              myapp = final.callPackage myapp { };
            })
          ];
        };
        # Go settings
        goVersion = 23;
      in
      {
        overlays.default = final: prev: {
          go = final."go_1_${toString goVersion}";
        };
        packages.default = pkgs.myapp;
        devShells = {
          # Shell for app dependencies.
          #
          #     nix develop
          #
          # Use this shell for developing your app.
          default = pkgs.mkShell {
            inputsFrom = [ 
            pkgs.myapp 
            ];
            packages = with pkgs; [
              # go (version is specified by overlay)
              go
              # goimports, godoc, etc.
              gotools
              # https://github.com/golangci/golangci-lint
              golangci-lint
              # lsp
              gopls
            ];
          };

          # Shell for poetry.
          #
          #     nix develop .#poetry
          #
          # Use this shell for changes to pyproject.toml and poetry.lock.
          poetry = pkgs.mkShell {
            packages = [ pkgs.poetry ];
          };
        };
        legacyPackages = pkgs;
      }
    );
}
