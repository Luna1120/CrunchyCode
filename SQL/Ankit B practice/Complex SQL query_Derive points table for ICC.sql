
select team_played as Team_name, count(team_played) as no_of_matches_played, sum(win_flag) as no_of_matches_won,
count(1)-sum(win_flag) as no_of_losses from 
(select Team_1 as team_played, case when Team_1=Winner then 1 else 0 end as win_flag from icc_world_cup
union all
select Team_2 as team_played, case when Team_2=Winner then 1 else 0 end as win_flag from icc_world_cup
)A
group by Team_name;

select * from icc_world_cup;