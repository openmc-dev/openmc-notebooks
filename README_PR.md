PR Checklist for `k_eff_search_with_tally_derivatives.ipynb`

- [ ] Notebook split into logical cells with explanatory text.
- [ ] Implementation left intact (functions: `build_model`, `run_with_gradient`, `gradient_based_search`, `builtin_keff_search`, `compare_optimization_methods`).
- [ ] Added small experiment cells (`run_experiments`, `plot_history`) for sensitivity testing.
- [ ] Added `requirements.txt` and `setup.sh` with recommended installation steps.
- [ ] Added quick setup instructions in a notebook cell (call `print_setup_instructions()`).
- [ ] Verified notebook JSON structure (cells have `metadata.language`, original cell ids preserved where applicable).

Notes for reviewers:
- OpenMC is recommended to be installed from `conda-forge`. The `setup.sh` creates a conda environment using conda-forge packages.
- Experiments in the notebook are intentionally conservative (low batches/particles) for quick smoke tests; users should increase them for production-quality results.
- Running the notebook will launch OpenMC simulations that produce HDF5 and statepoint files in the working directory. Consider running in a clean directory or adding `.gitignore` entries for `statepoint.*.h5`, `summary.h5`, and `tallies.out`.

Suggested follow-ups before merging:
- Add `.gitignore` entries for OpenMC outputs.
- Add CI smoke test that runs a single quick `run_with_gradient` with very small batches (if possible in CI environment).
- Optionally pin dependency versions in `requirements.txt` or a `environment.yml` file.
