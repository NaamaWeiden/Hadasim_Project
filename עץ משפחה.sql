USE FamilyTree;
GO

CREATE TABLE persons (
    Person_Id INT PRIMARY KEY,
    Personal_Name VARCHAR(50),
    Family_Name VARCHAR(50),
    Gender VARCHAR(10),
    Father_Id INT,
    Mother_Id INT,
    Spouse_Id INT
);

CREATE TABLE family_tree (
    Person_Id INT,
    Relative_Id INT,
    Connection_Type VARCHAR(50),
    PRIMARY KEY (Person_Id, Relative_Id),
    FOREIGN KEY (Person_Id) REFERENCES persons(Person_Id),
    FOREIGN KEY (Relative_Id) REFERENCES persons(Person_Id)
);



INSERT INTO persons (Person_Id, Personal_Name, Family_Name, Gender, Father_Id, Mother_Id, Spouse_Id) 
VALUES 
(1, 'David', 'Cohen', 'Male', NULL, NULL, 2),
(2, 'Sarah', 'Cohen', 'Female', NULL, NULL, NULL),
(3, 'Michael', 'Cohen', 'Male', 1, 2, NULL),
(4, 'Rachel', 'Cohen', 'Female', 1, 2, NULL);

SELECT * FROM persons;

--השלמת בני זוג חסרים
UPDATE p2
SET p2.Spouse_Id = p1.Person_Id
FROM persons p1
JOIN persons p2 
    ON p1.Spouse_Id = p2.Person_Id  
WHERE p1.Spouse_Id IS NOT NULL  
AND p2.Spouse_Id IS NULL  
AND p1.Person_Id <> p2.Person_Id; 



--הכנסת אב/אם
--הכנסת בן/בת זוג

INSERT INTO family_tree (Person_Id, Relative_Id, Connection_Type)
SELECT 
    p1.Person_Id,  
    p2.Person_Id, 
    CASE 
        WHEN p1.Person_Id = p2.Father_Id THEN 'Father'
        WHEN p1.Person_Id = p2.Mother_Id THEN 'Mother'
        WHEN p1.Person_Id = p2.Spouse_Id THEN 'Spouse'
       
    END AS Connection_Type
FROM persons p2
JOIN persons p1 
    ON p1.Person_Id = p2.Father_Id  
    OR p1.Person_Id = p2.Mother_Id  
    OR p1.Person_Id = p2.Spouse_Id  
WHERE (p2.Father_Id IS NOT NULL OR p2.Mother_Id IS NOT NULL OR p2.Spouse_Id IS NOT NULL)
AND NOT EXISTS (
    SELECT 1
    FROM family_tree ft
    WHERE ft.Person_Id = p2.Person_Id
    AND ft.Relative_Id = p1.Person_Id
);

--הכנסת  אח/אחות

INSERT INTO family_tree (Person_Id, Relative_Id, Connection_Type)
SELECT 
    p1.Person_Id, 
    p2.Person_Id,
    CASE 
        WHEN p2.Gender = 'Male' THEN 'Brother'
        WHEN p2.Gender = 'Female' THEN 'Sister'
    END AS Connection_Type
FROM persons p1
JOIN persons p2 
    ON (p1.Father_Id = p2.Father_Id OR p1.Mother_Id = p2.Mother_Id)
    AND p1.Person_Id <> p2.Person_Id
WHERE NOT EXISTS (
    SELECT 1
    FROM family_tree ft
    WHERE ft.Person_Id = p1.Person_Id
    AND ft.Relative_Id = p2.Person_Id
);


--הכנסת בן/בת
    
INSERT INTO family_tree (Person_Id, Relative_Id, Connection_Type)
SELECT 
    parent.Person_Id,
    child.Person_Id,
    CASE 
        WHEN child.Gender = 'Male' THEN 'Son'
        WHEN child.Gender = 'Female' THEN 'Daughter'
    END AS Connection_Type
FROM persons child
JOIN persons parent 
    ON child.Father_Id = parent.Person_Id
    OR child.Mother_Id = parent.Person_Id
WHERE NOT EXISTS (
    SELECT 1
    FROM family_tree ft
    WHERE ft.Person_Id = parent.Person_Id
    AND ft.Relative_Id = child.Person_Id
);

	

select * from family_tree



