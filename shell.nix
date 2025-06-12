{ pkgs ? import <nixpkgs> {} } : 

pkgs.mkShell{
  nativeBuildInputs = with pkgs; [
    python313Packages.pillow
    python313Packages.opencv4
  ];

  shellHook = ''
    echo "Shell prepared!"
  '';
}
