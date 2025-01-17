from typing import Union, Generic, TypeVar, List, Dict, Iterator

T = TypeVar('T')


class Exercise(Generic[T]):
    def __init__(self, type_: str) -> None:
        self._type = type_

    @property
    def type(self) -> str:
        return self._type

    def perform(self, *args) -> T:
        raise NotImplementedError('Plain exercise!')


class VowelsExercise(Exercise[int]):
    def __init__(self) -> None:
        super().__init__("vowels")

    def perform(self, text: str) -> int:
        return sum(1 for c in text if c.lower() in 'aeiou')


class NumberPyramid(Exercise[str]):
    def __init__(self) -> None:
        super().__init__('number_pyramid')

    def perform(self, size: int) -> str:
        return '\n'.join(''.join(map(str, range(1, i + 1))) for i in range(1, size + 1))
        # return '\n'.join([''.join(str(e + 1) for e in [*range(c)]) for c in range(1, size + 1)])


class MaxNumber(Exercise[int]):
    def __init__(self) -> None:
        super().__init__('max')

    def perform(self, nums: List[int]) -> int:
        return max(nums)
        # return sorted(nums)[-1] # OBIOUSLY THIS IS NOT OPTIMIZED! DO NOT CARE ABOUT THIS!


class EvenNumbers(Exercise[List[int]]):
    def __init__(self) -> None:
        super().__init__('even_numbers')

    def perform(self, n: int) -> List[int]:
        return [i for i in range(1, n + 1) if i % 2 == 0]


class AverageNumber(Exercise[float]):
    def __init__(self) -> None:
        super().__init__('average_number')

    def perform(self, lst: List[int]) -> float:
        return sum(lst) / len(lst)


class WordInString(Exercise[str]):
    def __init__(self) -> None:
        super().__init__('word_in_string')

    def _predicate(self, word: str, list_words: List[str]) -> bool:
        return word in list_words

    def perform(self, word: str, list_words: List[str]) -> str:
        return "yes" if self._predicate(word, list_words) else "no!"


class SquareCubeNumber(Exercise[Iterator[Dict[str, int]]]):
    def __init__(self) -> None:
        super().__init__('square_cube_number')

    def perform(self, n: int) -> Iterator[Dict[str, int]]:
        return map(lambda x: {"i": x, "i^2": x ** 2, "i^3": x ** 3}, range(1, n))


class TriangleBackwards(Exercise[str]):
    def __init__(self) -> None:
        super().__init__('triangle_backwards')

    def perform(self, n: int) -> str:
        return "\n".join("*" * i for i in range(n, 0, -1))


class ReversedString(Exercise[str]):
    def __init__(self) -> None:
        super().__init__('reversed_string')

    def perform(self, s: str) -> str:
        return s[::-1]
        
class FirstMultipliers(Exercise[List[int]]):
    def __init__(self) -> None:
        super().__init__('first_multipliers')

    def perform(self, n: int, m: int) -> List[int]:
      return [i * m for i in range(1, n +1)]


def main() -> None:
    exercise = VowelsExercise()
    print(exercise.perform("hola"))

    exercises = [VowelsExercise(), NumberPyramid(), MaxNumber(), EvenNumbers(), WordInString(), SquareCubeNumber(),
                 TriangleBackwards(), ReversedString()]
    dictionaries = list(map(lambda x: {"type": x.type, "instance": x}, exercises))

    # Why we should do this?
    """
    Well, it might be useful in the future, we'll be able to search for exercises 
    with an specific user input 
    """

    exercise = NumberPyramid()
    print(search_exercise('number_pyramid', dictionaries).perform(5))
    print(exercise.perform(5))


def search_exercise(exercise: Union[str, Exercise], dictionaries: List[Dict]) -> Exercise:
    if isinstance(exercise, str):
        return search_exercise_str(exercise, dictionaries)
    elif not isinstance(exercise, Exercise):
        raise RuntimeError("You're not supposed to do this!")

    pass  # Directly exercise implementation isn't necessary 'til now, i'll add it on the next days


def search_exercise_str(exercise: str, dictionaries: List[Dict]) -> Union[Exercise, None]:
    insensitive = lambda x: str(x).casefold()
    spaced = lambda x: insensitive(x).replace('_', ' ')

    for dictionary in dictionaries:
        type_ = dictionary['type']
        if not type_ == insensitive(exercise) and not spaced(type_) == spaced(exercise):
            continue

        return dictionary['instance']
    return None


if __name__ == '__main__':
    main()
