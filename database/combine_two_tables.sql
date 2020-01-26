SELECT FirstName, LastName, City, State
FROM person
LEFT JOIN Address ON Person.PersonId = Address.PersonId;
