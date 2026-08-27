from hashlib import md5, sha256
from pathlib import Path
import gzip
import subprocess

root = Path(__file__).resolve().parent.parent
packages = root / "Packages"
packages_gz = root / "Packages.gz"
release = root / "Release"

# Normalize the compressed index from the committed plain Packages file.
plain = packages.read_bytes()
with gzip.GzipFile(filename=str(packages_gz), mode="wb", compresslevel=9, mtime=0) as stream:
    stream.write(plain)

def digest(path: Path, algorithm: str) -> str:
    h = md5() if algorithm == "md5" else sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

def line(path: Path, algorithm: str) -> str:
    return f" {digest(path, algorithm)}  {path.stat().st_size} {path.name}"

release_text = """Label: Home Visual Accent
Suite: stable
Codename: home-visual-accent
Version: 1.0
Date: Thu, 27 Aug 2026 13:40:00 +0000
Architectures: iphoneos-arm64
Components:
Description: Home Visual Accent rootless iOS tweak and theme repository
MD5Sum:
{md5_packages}
{md5_gz}
SHA256:
{sha_packages}
{sha_gz}
""".format(
    md5_packages=line(packages, "md5"),
    md5_gz=line(packages_gz, "md5"),
    sha_packages=line(packages, "sha256"),
    sha_gz=line(packages_gz, "sha256"),
)
release.write_text(release_text)
subprocess.run(["gzip", "-t", str(packages_gz)], check=True)
print(f"Packages: {packages.stat().st_size} bytes")
print(f"Packages.gz: {packages_gz.stat().st_size} bytes")
print(release_text, end="")
