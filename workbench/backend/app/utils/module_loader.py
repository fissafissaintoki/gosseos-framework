from pathlib import Path

MODULES = {
    "gosseos_core": "GOSSEOS_CORE.md",
    "integrity_kernel": "INTEGRITY_KERNEL.md",
    "mode_specifications": "MODE_SPECIFICATIONS.md",
    "knowledgeos_core": "KNOWLEDGEOS_CORE.md",
    "artifact_registry": "ARTIFACT_REGISTRY_SPEC.md",
}

_PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def load_module(name: str) -> str:
    if name not in MODULES:
        raise KeyError(f"Unknown module '{name}'. Valid keys: {list(MODULES.keys())}")

    path = _PROMPTS_DIR / MODULES[name]
    if not path.exists():
        raise FileNotFoundError(
            f"Prompt module '{name}' not found at expected path: {path}. "
            "Ensure the markdown file exists in workbench/backend/app/prompts/."
        )

    return path.read_text(encoding="utf-8")


def load_all_modules() -> dict[str, str]:
    return {name: load_module(name) for name in MODULES}
