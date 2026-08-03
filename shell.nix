{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  buildInputs = (with pkgs; [

    python3
    python3Packages.pip
    python3Packages.virtualenv

    mypy
    ruff

    stdenv.cc.cc.lib
    
  ]);

  shellHook = ''
    mypy --version
    ruff --version
    python3 --version
  '';
}
