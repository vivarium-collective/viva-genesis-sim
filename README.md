# viva-genesis-sim

The **simulator** for the viva-genesis research program: the process-bigraph
composites, processes, and genuine-engine bridges that model the origin of life,
eukaryogenesis, and the origin of multicellularity.

This repository was **extracted from** the
[`viva-genesis`](https://github.com/vivarium-collective/viva-genesis) workspace so
that the two concerns live and version independently:

| repo | owns |
|------|------|
| **viva-genesis-sim** (this) | the `viva_genesis` Python package — the computational model (composites, processes, transport/geochemistry/electrochemistry/heredity/bioenergetics engines, viz) |
| **viva-genesis** | the *scientific content* — investigations and studies (`workspace/`), which **reference** a pinned version of this simulator |

The import path is unchanged: this package still installs as `viva_genesis`, so a
study's `baseline.composite: viva_genesis.composites.<…>` resolves exactly as before.

## Install

```bash
# core simulator (framework-free)
uv pip install "git+https://github.com/vivarium-collective/viva-genesis-sim.git@v0.1.0"
```

The **core** install is independent of the investigation framework —
`import viva_genesis` pulls in no `vivarium-workbench` / `viva-superpowers` /
`discovery_engine`, and most composites load on demand by dotted path.

### Optional extras

```bash
uv pip install "viva-genesis-sim[workspace] @ git+…@v0.1.0"   # workspace tooling + viz + the 2 composite_generator composites
uv pip install "viva-genesis-sim[membrane] @ git+…@v0.1.0"    # viva-openmm (Martini 3 CG MD)
uv pip install "viva-genesis-sim[spatial]  @ git+…@v0.1.0"    # viva-cpm (Rust Cellular Potts)
```

- **`workspace`** — `vivarium-workbench`, `viva-superpowers`, `viva-discovery-engine`.
  Needed only for the workspace-audit/lint helpers (`lint_checks`, `build_hook` —
  lazily imported and invoked *by* the framework), the `visualizations/` classes,
  and 2 of ~60 composites (`endogenous_boundary`, `physical_reproduction`) that
  build via `viva_superpowers.composite_generator`. The viva-genesis workspace
  installs this automatically because it depends on the framework anyway.

> **Follow-up:** the last framework call sites (2 composites + 2 lazy tooling
> imports) can be lifted so the simulator is 100% framework-free. Until then they
> live here behind the optional `workspace` extra. dolfinx (via `viva-fenics`) is
> conda-only and runs under that wrapper's pixi env; the Fenics transport classes
> register import-safe in a plain uv venv but only *run* there.

## Versioning

Tagged releases (`vMAJOR.MINOR.PATCH`). `viva-genesis` pins a specific tag via
`[tool.uv.sources]`, so every study records exactly which simulator built its runs.
