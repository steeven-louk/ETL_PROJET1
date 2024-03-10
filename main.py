from pipeline.pipeline import execute_pipeline


def main():
    # chemin vers le fichier de configuration yaml du pipeline
    pipeline_file = "./config/pipeplane_config.yaml"

    # execution du pipeline
    execute_pipeline(pipeline_file)


if __name__ == "__main__":
    main()
