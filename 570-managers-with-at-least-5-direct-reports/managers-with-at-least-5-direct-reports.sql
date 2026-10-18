select e.name from Employee e inner join Employee em
on e.id = em.managerId 
GROUP BY e.id, e.name
HAVING COUNT(em.id) >= 5;