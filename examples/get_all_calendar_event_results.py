import worldathletics

import asyncio

client = worldathletics.WorldAthletics()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def main():
    offset = 0
    limit = 100
    
    while True:
        response = await client.get_calendar_events(
            hide_competitions_with_no_results=True,
            limit=limit,
            region_type='world',
            offset=offset,
            show_options_with_no_hits=False,
            order_direction='Ascending',
            competition_group_id=None,
            competition_subgroup_id=None,
            discipline_id=None,
            end_date=None,
            permit_level_id=None,
            query=None,
            ranking_category_id=None,
            region_id=None,
            start_date=None,
        )
        for competition in response.get_calendar_events.results:
            print(competition.name, '[' + competition.date_range + ']')
            response = await client.get_calendar_competition_results(
                competition_id=competition.id
            )
            for event_title in response.get_calendar_competition_results.event_titles:
                print('-', event_title.event_title)
                for event in event_title.events:
                    print('--', event.event)
                    for race in event.races:
                        print('---', race.race)
                        for result in race.results:
                            print('----', result.competitor.name, '[' + str(result.competitor.iaaf_id) + ']' if result.competitor.iaaf_id else '', result.mark)

        if len(response.get_calendar_events.results) < limit:
            break
        offset += limit

if __name__ == '__main__':    
    asyncio.run(main())
