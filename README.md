> [!WARNING]
> **This repository has been archived as of 2026-01-12.** The functionality has been migrated and expanded upon in the [WILDS WDL Library](https://github.com/getwilds/wilds-wdl-library) as the [`ww-leukemia` pipeline](https://github.com/getwilds/wilds-wdl-library/tree/main/pipelines/ww-leukemia). Please refer to that instance for the latest versions, documentation, and updates.

# ww-vc-trio
[![Project Status: Experimental – Useable, some support, not open to feedback, unstable API.](https://getwilds.org/badges/badges/experimental.svg)](https://getwilds.org/badges/#experimental)

This WILDS WDL workflow takes samples through a standard alignment protocol and identifies variants using a trio of well-established variant callers. Finally, the workflow narrows it down to variants of confidence by analyzing consensus amongst the three variant callers.

## Usage

For Fred Hutch users that are new to WDL, we recommend using [PROOF](https://sciwiki.fredhutch.org/dasldemos/proof-how-to/) to submit this workflow directly to the on-premise HPC cluster, as it simplifies interaction with Cromwell and provides a user-friendly front-end for job submission and tracking. For users outside of Fred Hutch or more advanced users who would like to run the workflow locally, command line execution is relatively straightforward: 
```
java -jar cromwell-86.jar run ww-vc-trio.wdl \
    --inputs ww-vc-trio-inputs.json \
    --options ww-vc-trio-options.json
```
Although Cromwell is demonstrated here, this pipeline is not specific to Cromwell and can be run using whichever WDL execution method you prefer ([miniwdl](https://github.com/chanzuckerberg/miniwdl), [Terra](https://terra.bio/), [HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflows.html), etc.).

## Support

For questions, bugs, and/or feature requests, reach out to the Fred Hutch Data Science Lab (DaSL) at wilds@fredhutch.org, or open an issue on our [issue tracker](https://github.com/getwilds/ww-vc-trio/issues).

## Contributing

If you would like to contribute to this WILDS WDL workflow, see our [contribution guidelines](.github/CONTRIBUTING.md) as well out our [WILDS Contributor Guide](https://getwilds.org/guide/) for more details.

## License

Distributed under the MIT License. See `LICENSE` for details.
