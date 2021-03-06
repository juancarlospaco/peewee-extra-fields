#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copied from http://docs.peewee-orm.com/en/latest/peewee/quickstart.html


from datetime import date
from peewee import Model, SqliteDatabase
from peewee_extra_fields import *
from peewee_extra_fields import exceptions


db = SqliteDatabase('testing.db')


class Person(Model):  # All peewee_extra_fields.
    name = CharFieldCustom()
    birthday = PastDateField()
    cuit = ARCUITField()
    postal_code = ARZipCodeField()
    country = CountryISOCodeField()
    currency = CurrencyISOCodeField()
    language = LanguageISOCodeField()
    age = PositiveSmallIntegerField()
    interests = CSVField()
    mail = EmailField()
    ip = IPAddressField()
    color = ColorHexadecimalField()
    hexa = SmallHexadecimalField()
    json = JSONField()
    files = FileField()
    text = TextField(validators=["test_text"])

    class Meta:
        database = db


if __name__ in "__main__":
    db.create_tables([Person], safe=True)
    file = open('testing.db', "rb")  # Reading the file in binary form

    zoe = Person(name="Zoe", birthday=date(1985, 1, 1), cuit="20-30900000-6",
                 postal_code="1010", country="ar", currency="usd",
                 language="en", age=30, interests="python,peewee",
                 mail="Zoe@Example.com", ip="10.0.0.1", color="#fe0", hexa="2f",
                 json=[1, 2, 3, 4, 5], files=file, text="test_text")

    zoe.save()

    try:
        zoe.text = "test_text_"
        zoe.save()
    except exceptions.ValidationError:  # Attempt to fail
        pass


    del zoe  # Bye Zoe.

    zoe = Person.get(Person.name == "Zoe")  # Zoe is back.
    print(f"""Name:  {zoe.name},        Python Type: {type(zoe.name)}.
          Birthday:  {zoe.birthday},    Python Type: {type(zoe.birthday)}.
          CUIT:      {zoe.cuit},        Python Type: {type(zoe.cuit)}.
          Postal:    {zoe.postal_code}, Python Type: {type(zoe.postal_code)}.
          Age:       {zoe.age},         Python Type: {type(zoe.age)}.
          interests: {zoe.interests},   Python Type: {type(zoe.interests)}.
          Country:   {zoe.country},     Python Type: {type(zoe.country)}.
          Currency:  {zoe.currency},    Python Type: {type(zoe.currency)}.
          Language:  {zoe.language},    Python Type: {type(zoe.language)}.
          Mail:      {zoe.mail},        Python Type: {type(zoe.mail)}.
          IP:        {zoe.ip},          Python Type: {type(zoe.ip)}.
          Color:     {zoe.color},       Python Type: {type(zoe.color)}.
          Hexa:      {zoe.hexa},        Python Type: {type(zoe.hexa)}.
          Json:      {zoe.json},        python Type: {type(zoe.json)}.
          File:      {zoe.files},        python Type: {type(zoe.files.file_path)}.
          Text:      {zoe.text},        python Type: {type(zoe.text)}.
""")
