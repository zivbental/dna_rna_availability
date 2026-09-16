# YLR019W
Status: ok. Length: 1422 nt. Measured usable bases: 851. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 851 | 0.1582 | 0.1709 |
| rnafold | ok | 851 | 0.1570 | 0.1636 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 350 | 0.0842 | -0.0443 |
| seed_p | 350 | 0.0840 | -0.0080 |
| seed_p_vs_seed_pars | 266 | 0.0432 | -0.0211 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
