from utility.note import Note


class NoteComparator(object):
    """класс, предоставляющий методы для сравнения заметок по времени"""
    @staticmethod
    def compare_two_notes(note_1: Note, note_2: Note):
        """функция сравнивающая две заметки на предмет перекрытия по времени"""
        # если даты разные, то сразу выходим
        if note_1.get_date() != note_2.get_date():
            return
        # вводим переменные, соответствующие времени начала и окончания текущих заметок
        note_start_1 = note_1.get_start()
        note_start_2 = note_2.get_start()
        note_end_1 = note_1.get_end()
        note_end_2 = note_2.get_end()
        exception_message = "Заметки \"" + note_1.get_title() + "\" и \"" + note_2.get_title()
        exception_message += "\" перекрываются по времени"
        # сравниваем время начала и окончания
        if note_start_1 < note_end_2 <= note_end_1:
            raise Exception(exception_message)
        if note_start_1 <= note_start_2 < note_end_1:
            raise Exception(exception_message)
        if note_start_2 <= note_start_1 < note_end_2:
            raise Exception(exception_message)
        if note_start_2 < note_end_1 <= note_end_2:
            raise Exception(exception_message)

    @staticmethod
    def compare_note_with_array(note: Note, array):
        """сравнение заметки со списком заметок"""
        for _ in array:
            assert _, Note
            NoteComparator.compare_two_notes(note, _)

    @staticmethod
    def compare_notes_in_array(array):
        """сравнение заметок внутри массива"""
        for i in range(len(array)):
            for j in range(i, len(array)):
                assert array[i], Note
                assert array[j], Note
                NoteComparator.compare_two_notes(array[i], array[j])
