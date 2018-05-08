from utility.note import Note

exception_message = 'Несовместимые заметки'


class NoteComparator(object):
    """
        если заметки перекрывают друг друга, то выкидываем ошибку
    """
    @staticmethod
    def compare_two_notes(note_1: Note, note_2: Note):
        assert note_1, Note
        assert note_2, Note
        note_start_1 = note_1.get_start()
        note_start_2 = note_2.get_start()
        note_end_1 = note_1.get_end()
        note_end_2 = note_2.get_end()

        if note_start_1 < note_end_2 < note_end_1:
            raise Exception(exception_message)
        if note_start_1 < note_start_2 < note_end_1:
            raise Exception(exception_message)
        if note_start_2 < note_start_1 < note_end_2:
            raise Exception(exception_message)
        if note_start_2 < note_end_1 < note_end_2:
            raise Exception(exception_message)

    """
        сравнение заметки со списком заметок
    """
    @staticmethod
    def compare_note_with_array(note, array):
        for _ in array:
            assert _, Note
            NoteComparator.compare_two_notes(note, _)

    """
        сравнение заметок внутри массива    
    """
    @staticmethod
    def compare_notes_in_array(array):
        for i in range(len(array)):
            for j in range(i, len(array)):
                assert array[i], Note
                assert array[j], Note
                NoteComparator.compare_two_notes(111111, array[j])
