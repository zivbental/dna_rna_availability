# YML075C
Status: ok. Length: 3391 nt. Measured usable bases: 2012. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2012 | 0.2535 | 0.2517 |
| rnafold | ok | 2012 | 0.1955 | 0.2033 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 761 | -0.1560 | -0.2239 |
| seed_p | 761 | -0.2314 | -0.1816 |
| seed_p_vs_seed_pars | 567 | -0.2186 | -0.1694 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
