from dataclasses import FrozenInstanceError, dataclass


@dataclass(init=False)
class CarWithoutInit:
    manufacturer: str = None


@dataclass(repr=False)
class CarWithoutRepr:
    manufacturer: str = None


@dataclass(eq=False)
class CarWithoutEq:
    manufacturer: str = None


@dataclass(order=True)
class CarOrderable:
    seats: int = None
    doors: int = None


@dataclass(frozen=True)
class ImmutableCar:
    seats: int = None


@dataclass()
class Car:
    manufacturer: str = None
    model: str = None
    color: str = None
    length: float = None
    seats: int = None
    is_suv: bool = None


def main():
    new_car = Car(
        manufacturer="Tesla",
        model="Model X",
        color="blue",
        length=5.0,
        seats=5,
        is_suv=True,
    )
    print(new_car)
    if new_car.is_suv:
        print(f"{new_car.manufacturer} {new_car.model} is a SUV")

    # should show a warning for a wrong type. is_suv should be a boolean
    # and we use a string instead
    another_car = Car(manufacturer="VW", is_suv="No")
    print(another_car)


def with_init():
    # a class without default init method
    try:
        CarWithoutInit(manufacturer="Tesla")
    except TypeError:
        print("CarWithoutInit could not be created")

    new_car_without_init = CarWithoutInit()
    new_car_without_init.manufacturer = "BMW"
    print(new_car_without_init)


def with_repr():
    # a class without default repr method
    new_car_without_repr = CarWithoutRepr(manufacturer="Audi")
    print(new_car_without_repr)


def equals():
    # equality comparison
    tesla_a = Car(manufacturer="Tesla")
    tesla_b = Car(manufacturer="Tesla")
    bmw = Car(manufacturer="BMW")
    print("tesla_a == tesla_b :", tesla_a == tesla_b)
    print("tesla_a is tesla_b :", tesla_a is tesla_b)
    print("tesla_a is tesla_a :", tesla_a is tesla_a)
    print("bmw == tesla :", bmw == tesla_a)

    # equality comparison disabled
    tesla_a = CarWithoutEq(manufacturer="Tesla")
    tesla_b = CarWithoutEq(manufacturer="Tesla")
    print("tesla_a == tesla_b :", tesla_a == tesla_b)
    print("tesla_a is tesla_b :", tesla_a is tesla_b)
    print("tesla_a is tesla_a :", tesla_a is tesla_a)


def order():
    # order by seats
    car_with_2_seats = CarOrderable(seats=2)
    car_with_3_seats = CarOrderable(seats=3)
    car_with_4_seats = CarOrderable(seats=4)
    print("2 > 3 :", car_with_2_seats > car_with_3_seats)
    print("4 > 3 :", car_with_4_seats > car_with_3_seats)
    print("2 <= 4 :", car_with_2_seats <= car_with_4_seats)

    # order by seats and doors
    car_with_2_seats_and_3_doors = CarOrderable(seats=2, doors=3)
    car_with_3_seats_and_2_doors = CarOrderable(seats=3, doors=2)
    print(
        "2,3 > 3,2 :",
        car_with_2_seats_and_3_doors >= car_with_3_seats_and_2_doors,
    )
    print(
        "2,3 < 3,2 :",
        car_with_2_seats_and_3_doors <= car_with_3_seats_and_2_doors,
    )

    car_with_3_seats_and_3_doors = CarOrderable(seats=3, doors=3)
    car_with_3_seats_and_2_doors = CarOrderable(seats=3, doors=2)
    print(
        "3,3 > 3,2 :",
        car_with_3_seats_and_3_doors >= car_with_3_seats_and_2_doors,
    )
    print(
        "3,3 < 3,2 :",
        car_with_3_seats_and_3_doors <= car_with_3_seats_and_2_doors,
    )


def frozen():
    immutable_car = ImmutableCar(seats=5)
    print(immutable_car)
    immutable_car.seats = 6


if __name__ == "__main__":
    main()
    with_init()
    with_repr()
    equals()
    order()
    frozen()
