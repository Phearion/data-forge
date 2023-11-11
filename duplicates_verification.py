import pandas as pd


class DuplicatesVerification:
    """
    Duplicate verification class to verify if there are duplicates in the CSV files.
    """

    def __init__(self, file):
        self.file = file
        self.base_nb_observations = 0
        self.nb_duplicates = 0  # nb of duplicates that were removed

    def verify_duplicates(self):
        """
        Verify if there are duplicates in the CSV files.
        """
        df = pd.read_csv(self.file, encoding="cp1252", delimiter=";")
        self.base_nb_observations = df.shape[0]

        # check for duplicates in the input column
        df_duplicates = df[df.duplicated(subset=["input"], keep=False)]

        if df_duplicates.empty:
            print(f"{self.file}: no duplicates")
        else:
            # remove duplicates
            df.drop_duplicates(subset=["input"], keep="first", inplace=True)

            # save the dataframe to a new csv file
            df.to_csv(self.file, index=False, encoding="cp1252", sep=";")
            self.nb_duplicates = self.base_nb_observations - df.shape[0]
            print(f"{self.file}: {self.nb_duplicates} duplicates removed")
