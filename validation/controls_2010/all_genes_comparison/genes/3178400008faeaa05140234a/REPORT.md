# YIL047C
Status: ok. Length: 2709 nt. Measured usable bases: 1737. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1737 | 0.3000 | 0.2816 |
| rnafold | ok | 1737 | 0.2372 | 0.2256 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 913 | -0.0333 | -0.0130 |
| seed_p | 913 | -0.0621 | -0.0699 |
| seed_p_vs_seed_pars | 631 | -0.2899 | -0.2622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
