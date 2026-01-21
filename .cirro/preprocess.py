#!/usr/bin/env python3

# This script runs before the workflow launches on the head node.
# It must write out:
# - options.json: a dictionary of options for the workflow
# - inputs.1.json: a dictionary of inputs for the workflow
# NOTE: The use of the "inputs.x.json" pattern is to allow for multiple
#       inputs to be passed to the workflow. This is useful for running
#       multiple samples in series.
#       The behavior of the Cromwell executor is that any file with the
#       pattern "inputs.*.json" will be executed.

# The PreprocessDataset class is a helper
# which provides useful information about the inputs provided by the user.
# The two main attributes are:
# - ds.files: a DataFrame with the columns 'sample' and 'file'
# - ds.params: a dictionary of parameters passed in by the user
from cirro.helpers.preprocess_dataset import PreprocessDataset
import json
from cirro.api.models.s3_path import S3Path


def write_batch_file(ds: PreprocessDataset):
    # The table of BAM files which were input by the user is available
    # as `ds.files`: a DataFrame with the columns 'sample' and 'file'.
    # This table will be modified slightly to conform to the expected
    # format of the batch_file.tsv file which is used by the workflow.
    (
        ds.files
        .rename(
            columns=dict(
                sample="omics_sample_name",
                file="bamLocation"
            )
        )
        .assign(
            molecular_id=lambda d: d["omics_sample_name"]
        )
        .reindex(columns=["omics_sample_name", "molecular_id", "bamLocation"])
        # Note that the path "batch_file.tsv" is already specified in the
        # "ww_vc_trio.batchFile" param defined in process-input.json
        .to_csv("batch_file.tsv", sep="\t", index=False)
    )


def write_inputs(ds: PreprocessDataset):

    # Get the dict of inputs from the user
    inputs = ds.params["inputs"]

    # When the user selects the set of annovar protocols to run, it will be
    # passed in as a list of strings. This will be pasted into a single string
    # before passing into the workflow
    inputs["ww_vc_trio.annovar_protocols"] = ",".join(inputs["ww_vc_trio.annovar_protocols"])

    # Write out the complete set of inputs as a list (for logging purposes)
    write_json("inputs.json", [inputs])

    # Write out the single dict to inputs.1.json
    write_json("inputs.1.json", inputs)


def write_json(fp, obj, indent=4):
    """Helper to write a JSON file with a given object."""
    with open(fp, "wt") as handle:
        json.dump(obj, handle, indent=indent)


def write_options(ds: PreprocessDataset):

    # Get the dict of options from the user
    options = ds.params["options"]

    # Set up the scriptBucketName
    options["scriptBucketName"] = S3Path(options['final_workflow_outputs_dir']).bucket

    # Isolate the options arguments for the workflow
    write_json("options.json", options)


if __name__ == "__main__":

    # The PreprocessDataset is a helper class which provides useful information
    # about the inputs provided by the user.
    ds = PreprocessDataset.from_running()

    # Write out the batch_file.tsv
    write_batch_file(ds)

    # Write out the inputs to the workflow
    write_inputs(ds)

    # Write out the options for the workflow
    write_options(ds)
