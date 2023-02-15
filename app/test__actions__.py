from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from app import actions, models, schemas


def test_get_trainer():
    # Setup
    database = MagicMock(spec=Session)
    trainer = models.Trainer(id=1, name="Ash", birthdate="1990-01-01")
    database.query().filter().first.return_value = trainer

    # Execution
    result = actions.get_trainer(database, trainer_id=1)

    # Assertion
    assert result == trainer


def test_get_trainer_by_name():
    # Setup
    database = MagicMock(spec=Session)
    trainer1 = models.Trainer(id=1, name="Ash", birthdate="1990-01-01")
    trainer2 = models.Trainer(id=2, name="Gary", birthdate="1991-01-01")
    database.query(models.Trainer).filter(models.Trainer.name == "Ash").all.return_value = [trainer1]

    # Execution
    result = actions.get_trainer_by_name(database, name="Ash")

    # Assertion
    assert result == [trainer1], f"Expected [trainer1], but got {result} instead"

def Negative_test_get_trainer_by_name():
    database = MagicMock(spec=Session)
    trainer1 = models.Trainer(id=1, name="Ash", birthdate="1990-01-01")
    trainer2 = models.Trainer(id=2, name="Gary", birthdate="1991-01-01")
    database.query().filter().all.return_value = [trainer1, trainer2]

    # Execution
    result = actions.get_trainer_by_name(database, name="Misty")

    # Assertion
    assert result == [], f"Expected [], but got {result} instead"

def test_create_trainer():
    # Setup
    database = MagicMock(spec=Session)
    trainer = schemas.TrainerCreate(name="Ash", birthdate="1990-01-01")
    db_trainer = models.Trainer(id=1, name="Ash", birthdate="1990-01-01")
    database.add(db_trainer)
    database.commit.return_value = None
    database.refresh.return_value = None
    database.query(models.Trainer).filter(models.Trainer.id == 1).first.return_value = db_trainer

    # Execution
    result = actions.create_trainer(database, trainer)

    # Assertion
    assert result == db_trainer, f"Expected {db_trainer}, but got {result} instead"


def test_add_trainer_pokemon():
    # Setup
    database = MagicMock(spec=Session)
    pokemon = schemas.PokemonCreate(api_id=25, level=50)
    trainer_id = 1
    db_pokemon = models.Pokemon(api_id=25, level=50, name="Pikachu", trainer_id=trainer_id)
    database.add(db_pokemon)
    database.commit.return_value = None
    database.refresh.return_value = None

    # Execution
    result = actions.add_trainer_pokemon(database, trainer_id, pokemon)

    # Assertion
    assert result == db_pokemon, f"Expected {db_pokemon}, but got {result} instead"


def test_add_trainer_item():
    # Setup
    database = MagicMock(spec=Session)
    item = schemas.ItemCreate(name="Potion", quantity=1)
    trainer_id = 1
    db_item = models.Item(name="Potion", quantity=1, trainer_id=trainer_id)
    database.add.return_value = None
    database.commit.return_value = None
    database.refresh.return_value = None
    models.Item.__new__.return_value = db_item

    # Execution
    result = actions.add_trainer_item(database, item, trainer_id)

    # Assertion
    assert result == db_item


def test_get_items():
    # Setup
    database = MagicMock(spec=Session)
    item1 = models.Item(id=1, name="Potion", quantity=1, trainer_id=1)
    item2 = models.Item(id=2, name="Max Potion", quantity=2, trainer_id=2)
    database.query().offset().limit().all.return_value = [item1, item2]

    # Execution
    result = actions.get_items(database)

    # Assertion
    assert result == [item1, item2]
