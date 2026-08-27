# SpecialLock Package Repository

This private repository contains the reverted SpecialLock rootless iOS package requested for iOS 15 and Dopamine/ElleKit.

## Add to Sileo

Add the repository’s raw main URL:

```text
https://raw.githubusercontent.com/James1997s/speciallock-repo/main/
```

The repository uses a flat APT layout with `Release`, `Packages`, `Packages.gz`, and the package in `debs/`.

## Package

The current rollback build is `com.example.speciallock` version `0.1.0-66` for `iphoneos-arm64`. It restores the pre-full-screen renderer behavior.
