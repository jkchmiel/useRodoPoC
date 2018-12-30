import os
from subprocess import call


class SampleDataInTmp:

    @staticmethod
    def make_copy(source_dir: str, tmp_dir = 'tmp/', data_folder = 'data'):
        target_dir = f"{tmp_dir}{source_dir}"
        print(f"Create directory: {target_dir}")
        os.makedirs(target_dir, exist_ok=True)
        call(['cp', '-a', f"{source_dir}/{data_folder}", target_dir])


if __name__ == "__main__":
    SampleDataInTmp.make_copy("integrations/prestashop/data")
