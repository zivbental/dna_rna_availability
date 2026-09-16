# YDR072C
Status: ok. Length: 2326 nt. Measured usable bases: 1142. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1142 | 0.2836 | 0.2716 |
| rnafold | ok | 1142 | 0.2529 | 0.2505 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 482 | -0.2777 | -0.3797 |
| seed_p | 482 | -0.2352 | -0.2747 |
| seed_p_vs_seed_pars | 382 | -0.3686 | -0.3787 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
