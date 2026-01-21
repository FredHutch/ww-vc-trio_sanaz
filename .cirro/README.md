## Cirro Configuration

The files in this directory are used to configure the workflow for deployment on Cirro.
General guidance on how to deploy a workflow on Cirro can be found [here](https://docs.cirro.bio/pipelines/adding-pipelines/).

- `process-form.json`: Defines a webform which the user can make selections from to configure the workflow.
- `process-input.json`: Maps user inputs to a dict (Struct) which is passed to the headnode.
- `preprocess.py`: Script run by the headnode to create the `inputs.json` and `options.json` needed by the workflow, which incorporates user inputs.

### Form Inputs

Any form elements available using the React JSON Schema library can be used in the `process-form.json` file. The library documentation can be found [here](https://rjsf-team.github.io/react-jsonschema-form/).

In addition to those atomic types, the form can also be used for selecting [Pipeline References](https://docs.cirro.bio/features/pipelines/#pipeline-references).
In the case of this workflow, the BED file is a Pipeline Reference.
The user can upload a BED file on the Reference page, and then select it from the dropdown in the form.
This makes it easy to reuse the same reference file across multiple workflow runs.

The syntax for this type of feature is:

```
"bedLocation": {
    "title": "Regions of Interest (BED)",
    "description": "Select BED file which has been added to the References for this project.",
    "type": "string",
    "pathType": "references",
    "file": "**/genome_bed/**/regions.bed"
}
```

### Reference Genome

The reference genome is a required input for the workflow.
While the individual reference genome files could be sourced from any location, the Cirro platform provides
a set of reference genomes provided by [the iGenomes project](https://ewels.github.io/AWS-iGenomes/).

The prefix `s3://pubweb-references/igenomes/Homo_sapiens/GATK/GRCh37` contains the version of GRCh37
which has been indexed with the resources needed for running GATK analysis tools.
