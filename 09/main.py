from library_organizer import LibraryOrganizer
from library_repository import LibraryRepository

from dataset import DATASET
from library_program_run import library_program_run


if __name__ == "__main__":

    test1 = LibraryOrganizer()
    test1.process_data_set(DATASET)
    repository = LibraryRepository(test1)

    library_program_run(test1, repository)