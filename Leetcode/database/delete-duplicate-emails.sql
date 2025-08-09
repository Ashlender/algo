-- https://leetcode.com/problems/delete-duplicate-emails/description/
DELETE FROM Person WHERE id not in (SELECT min(id) FROM Person GROUP BY email)