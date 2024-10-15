{ pkgs ? import <nixpkgs> {} } : 

pkgs.mkShell{
  nativeBuildInputs = with pkgs; [
    python3
    python311Packages.pillow
    python311Packages.opencv4
  ];

  shellHook = ''
    echo "Shell prepared!"
  '';
}