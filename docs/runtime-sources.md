# Runtime source inventory — 2 November 2026

**This is verified provenance groundwork, not completed corresponding-source delivery or a reproducible-build claim.** The [machine-readable inventory](runtime-sources.json) records canonical URLs, exact tag commits, downloaded archive hashes, package versions and unresolved bindings. Source archives are retained in the local audit workspace; this document does not claim they have been published beside an APK. The source-delivery gate remains open; the application workflows and THIRD_PARTY.md files record the corresponding APK-upload hold.

## Observed inputs

The inventory checked the pre-filter baseline: all 513 Atelier prepared files and both Vitrine prepared ZIPs match their preparation receipts. All five cached runtime-download inputs for each application match the runtime lock digests. The R runtime reports R 4.6.0; Pyodide identifies Python 3.12.7, Pyodide 0.27.7, ABI 2024_0 and Emscripten 3.1.58.

| Component | Exact source commit | Collected source archive SHA-256 |
|---|---|---|
| [webr v0.6.0](https://github.com/r-wasm/webr/tree/f116a5e60e220182d09ac015837c88c454c663c5) | `f116a5e60e220182d09ac015837c88c454c663c5` | `208877f5cbe214af7d07aa3d6c7adb4107df51a8bcaec12ca1d349ec5cf3eb9d` |
| [shinylive v0.10.12](https://github.com/posit-dev/shinylive/tree/2726fe99c05ba4516cd002bef8d8f734be125133) | `2726fe99c05ba4516cd002bef8d8f734be125133` | `a6653e259eb8fbe974e8311ce3d76b1de3661495eadbcb9d0c5ca3454f946903` |
| [pyodide 0.27.7](https://github.com/pyodide/pyodide/tree/8250fdc3dc7bfd587fd8f4cc267e173095c58445) | `8250fdc3dc7bfd587fd8f4cc267e173095c58445` | `7147e54d4561eb65a916136b8cda10869118a1db39be401f7e01ac0f701ef679` |
| [r-shiny v1.13.0.8000](https://github.com/r-wasm/shiny/tree/ad8cadf9618b460f8362a8d1e1bb9e3f68789f25) | `ad8cadf9618b460f8362a8d1e1bb9e3f68789f25` | `3c774a133312d2c46f2d3dad95e55703300f5ac28fd5bbc908aa20353a101d7a` |

[R 4.6.0 source](https://cran.r-project.org/src/base/R-4/R-4.6.0.tar.gz) was downloaded with SHA-256 `b8dc9b4543660c7b596b87938df532394350360976527d344228ee0ed12e45ec`; that is a locally recorded digest, without an independent expected source digest. [CPython 3.12.7 source](https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tgz) matches the Pyodide recipe digest `73ac8fe780227bf371add8373c3079f42a0dc62deff8d612cd15a618082ab623`. WebR’s tagged R patches and 42 supporting-library recipe directories are retained in its source archive; the exact Flang gitlink source was also collected. These facts do not identify every binary build input.

## Vitrine R engine and packages

The WebR npm archive passes the integrity value pinned by shinylive. Of 167 engine WebR files compared, 166 are byte-identical; the sole `R.js` difference is exactly the transformation in the [tagged shinylive Makefile](https://github.com/posit-dev/shinylive/blob/2726fe99c05ba4516cd002bef8d8f734be125133/Makefile#L146).

Both `library.data.gz` and `library.js.metadata` match the published SHA-256 asset digests for [r-wasm/shiny v1.13.0.8000](https://github.com/r-wasm/shiny/releases/tag/v1.13.0.8000). Reading the image’s indexed DESCRIPTION files identifies 36 packages. Matching-version source archives for 32 ordinary packages were downloaded from CRAN or the dated Posit repository, and the exact `shiny` release source was collected. A matching version is not proof that the archive, any patches and the compiler inputs produced the installed bytes.

The image contains three additional fork versions with no captured source commit: `httpuv 1.6.6.9000`, `later 1.4.2.9000` and `sass 0.4.10.9000`. The [historical successful image build](https://github.com/r-wasm/shiny/actions/runs/26228930683) records reusable-workflow commit `0f8493df20b6b47d3621f16be81218926a09dad1`. Its logs endpoint now returns HTTP 410. The workflow used a moving `ghcr.io/r-wasm/webr:main` image; the WebR Dockerfile uses moving `r-wasm/rwasm`, `r-lib/pak@main` and Posit’s `latest` repository. Their historical resolved source versions and container digest have not been recovered.

## Atelier Python package scope

The original prepared distribution contains 31 lock-listed payloads: 21 selected wheels, required OpenBLAS, and nine unrelated shared-library/test ZIPs. Every payload matches its Pyodide lock hash and has a recipe in the exact Pyodide tag. Source archives for the 29 external package inputs were downloaded and checksum-verified against the pinned recipe or exact-version PyPI source metadata; two test-library sources are already in the Pyodide source archive. For pure-Python recipes that consume wheels, an exact-version source distribution remains a source candidate, not a proven rebuild of the wheel.

The intended filtered dependency closure has 22 payloads: the 21 wheels plus `openblas-0.3.26.zip`. Nine historical ZIPs outside that closure total 38,201,437 bytes: `cpp-exceptions-test`, `gdal`, `geos`, `libhdf5`, `libheif`, `libmagic`, `openssl`, `sharedlib-test` and `suitesparse`. They are recorded separately in the JSON; they must not be described as remaining selected dependencies. Eight focused preparation/publication tests passed for the filter repair. Full real-asset preparation, offline numerical execution and rebuilt APK validation are separate checks and are not asserted here.

Source license checks also exposed two upstream metadata cautions in historical unused payloads: the `libheif` lock labels version 1.12.0 while its checksum-pinned recipe downloads 1.17.3; the OpenSSL 1.1.1w source uses the OpenSSL and original SSLeay licenses, despite the recipe’s Apache-2.0 label. Preserve the source evidence rather than copying those recipe labels uncritically.

## Remaining build and delivery work

WebR’s release workflow uses `flang-wasm:main`, and the Flang source Makefile fetches an unpinned LLVM `wasm` branch. WebR release notes report Emscripten 4.0.8, while the gitlinked Flang Dockerfile defaults to 5.0.7. The checked WASM binaries have no producer metadata resolving that discrepancy. The full support-library, toolchain, JavaScript and font source/build-input closure has not been collected and rebuilt.

The next action is to obtain the exact existing R-image fork/container/dependency provenance, or replace that image with a freshly built version whose complete inputs are pinned and archived. Then document and exercise the source-build and installation steps, retain binary-to-source evidence, and publish durable matching source downloads beside any resumed binary upload. Bit-for-bit reproducibility requires its own comparison. No runtime or native rebuild was performed for this inventory, and the source-delivery gate remains open.
