"""viva_genesis visualization classes.

Registered pbg ``Visualization`` (``Step``) subclasses, one concern per module.
The workbench resolves ``address: local:<ClassName>`` by importing this package's
submodules and registering every subclass by name (see
vivarium_workbench.env_worker). Keep viz classes HERE (not at the package root)
so both the dashboard resolver and the readiness linter discover them.

Importing this package imports every submodule and re-exports its classes at the
package level, so ``build_core``'s non-recursive ``pkgutil.iter_modules`` walk
registers all viz classes from this one subpackage — no per-module re-export
shims at the package root are needed.
"""
import importlib as _importlib
import pkgutil as _pkgutil

for _mod_info in _pkgutil.iter_modules(__path__):
    _m = _importlib.import_module(f"{__name__}.{_mod_info.name}")
    for _name in dir(_m):
        if _name.startswith("_"):
            continue
        _obj = getattr(_m, _name)
        if isinstance(_obj, type):
            globals()[_name] = _obj
del _importlib, _pkgutil, _mod_info, _m, _name, _obj
