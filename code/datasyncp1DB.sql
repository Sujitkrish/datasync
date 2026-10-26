create database datasyncp1

create table super_market(
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(50),          
    DepartmentID int,
    Price	 decimal,                  
    StockQuantity int
);

select * from super_market
