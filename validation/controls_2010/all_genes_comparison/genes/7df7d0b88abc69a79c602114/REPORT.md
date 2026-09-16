# YBR218C
Status: ok. Length: 3778 nt. Measured usable bases: 1908. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1908 | 0.3089 | 0.2879 |
| rnafold | ok | 1908 | 0.2684 | 0.2653 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 513 | -0.1073 | -0.3344 |
| seed_p | 513 | -0.2538 | -0.2920 |
| seed_p_vs_seed_pars | 333 | -0.2591 | -0.3973 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
