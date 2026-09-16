# YBR243C
Status: ok. Length: 1347 nt. Measured usable bases: 793. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 793 | 0.3052 | 0.2825 |
| rnafold | ok | 793 | 0.1786 | 0.2131 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.2838 | -0.3006 |
| seed_p | 203 | -0.2952 | -0.2851 |
| seed_p_vs_seed_pars | 147 | -0.1548 | -0.1749 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
