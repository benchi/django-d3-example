MOCK_RESPONSE = '''
{
    "last_7_summary": {
        "me": {
            "meeting_hours": 170,
            "company_time_dollars": 21250,
            "num_total_meetings": 22,
            "num_recurring_meetings": 16,
            "percent_good_use": 17.234
        },
        "peers_at_title": {
            "meeting_hours": 105,
            "company_time_dollars": 16005,
            "num_total_meetings": 18,
            "num_recurring_meetings": 12,
            "percent_good_use": 36.234
        },
        "company": {
            "meeting_hours": 180,
            "company_time_dollars": 22250,
            "num_total_meetings": 23,
            "num_recurring_meetings": 12,
            "percent_good_use": 27.234
        }
    },
    "last_7_callouts": {
        "most_effective": [
            {"id": "uuidsomething", "name": "Team Standup", "is_recurring": true},
            {"id": "uuidsomething", "name": "1/1 Jimbo", "is_recurring": true},
            {"id": "uuidsomething", "name": "1/1 Bobbie", "is_recurring": true}
        ],
        "least_effective": [
            {"id": "uuidsomething", "name": "Operational Review", "is_recurring": true},
            {"id": "uuidsomething", "name": "Project Status", "is_recurring": true},
            {"id": "uuidsomething", "name": "SoS #72", "is_recurring": true}
        ],
        "most_expensive": [
            {"id": "uuidsomething", "name": "DevP Brown Bag", "is_recurring": true},
            {"id": "uuidsomething", "name": "Operational Revieww", "is_recurring": true},
            {"id": "uuidsomething", "name": "Standup", "is_recurring": true}
        ]
    },
    "last_3_months": {
        "me": [
            {
                "meeting_hours": 160,
                "company_time_dollars": 14250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 17.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 22050,
                "num_total_meetings": 20,
                "num_recurring_meetings": 15,
                "percent_good_use": 30.234
            },
            {
                "meeting_hours": 120,
                "company_time_dollars": 19250,
                "num_total_meetings": 23,
                "num_recurring_meetings": 17,
                "percent_good_use": 31.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 188250,
                "num_total_meetings": 24,
                "num_recurring_meetings": 18,
                "percent_good_use": 22.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 17750,
                "num_total_meetings": 21,
                "num_recurring_meetings": 16,
                "percent_good_use": 62.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 11250,
                "num_total_meetings": 30,
                "num_recurring_meetings": 16,
                "percent_good_use": 44.234
            },
            {
                "meeting_hours": 270,
                "company_time_dollars": 17250,
                "num_total_meetings": 29,
                "num_recurring_meetings": 16,
                "percent_good_use": 47.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 18250,
                "num_total_meetings": 28,
                "num_recurring_meetings": 20,
                "percent_good_use": 35.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 21330,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 32.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 22250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 33.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 11250,
                "num_total_meetings": 10,
                "num_recurring_meetings": 6,
                "percent_good_use": 40.234
            },
            {
                "meeting_hours": 140,
                "company_time_dollars": 10000,
                "num_total_meetings": 12,
                "num_recurring_meetings": 10,
                "percent_good_use": 41.234
            },
            {
                "meeting_hours": 170,
                "company_time_dollars": 21250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 17.234
            }
        ],
        "peers_at_title": [
            {
                "meeting_hours": 160,
                "company_time_dollars": 14250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 17.234
            },
            {
                "meeting_hours": 270,
                "company_time_dollars": 17250,
                "num_total_meetings": 29,
                "num_recurring_meetings": 16,
                "percent_good_use": 47.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 18250,
                "num_total_meetings": 28,
                "num_recurring_meetings": 20,
                "percent_good_use": 35.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 21330,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 32.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 22250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 33.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 11250,
                "num_total_meetings": 10,
                "num_recurring_meetings": 6,
                "percent_good_use": 40.234
            },
            {
                "meeting_hours": 140,
                "company_time_dollars": 10000,
                "num_total_meetings": 12,
                "num_recurring_meetings": 10,
                "percent_good_use": 41.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 22050,
                "num_total_meetings": 20,
                "num_recurring_meetings": 15,
                "percent_good_use": 30.234
            },
            {
                "meeting_hours": 120,
                "company_time_dollars": 19250,
                "num_total_meetings": 23,
                "num_recurring_meetings": 17,
                "percent_good_use": 31.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 188250,
                "num_total_meetings": 24,
                "num_recurring_meetings": 18,
                "percent_good_use": 22.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 17750,
                "num_total_meetings": 21,
                "num_recurring_meetings": 16,
                "percent_good_use": 62.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 11250,
                "num_total_meetings": 30,
                "num_recurring_meetings": 16,
                "percent_good_use": 44.234
            },
            {
                "meeting_hours": 170,
                "company_time_dollars": 21250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 17.234
            }
        ],
        "company": [
            {
                "meeting_hours": 130,
                "company_time_dollars": 188250,
                "num_total_meetings": 24,
                "num_recurring_meetings": 18,
                "percent_good_use": 22.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 17750,
                "num_total_meetings": 21,
                "num_recurring_meetings": 16,
                "percent_good_use": 62.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 11250,
                "num_total_meetings": 30,
                "num_recurring_meetings": 16,
                "percent_good_use": 44.234
            },
            {
                "meeting_hours": 270,
                "company_time_dollars": 17250,
                "num_total_meetings": 29,
                "num_recurring_meetings": 16,
                "percent_good_use": 47.234
            },
            {
                "meeting_hours": 170,
                "company_time_dollars": 21250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 17.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 18250,
                "num_total_meetings": 28,
                "num_recurring_meetings": 20,
                "percent_good_use": 35.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 21330,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 32.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 22250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 33.234
            },
            {
                "meeting_hours": 130,
                "company_time_dollars": 11250,
                "num_total_meetings": 10,
                "num_recurring_meetings": 6,
                "percent_good_use": 40.234
            },
            {
                "meeting_hours": 140,
                "company_time_dollars": 10000,
                "num_total_meetings": 12,
                "num_recurring_meetings": 10,
                "percent_good_use": 41.234
            },
            {
                "meeting_hours": 160,
                "company_time_dollars": 14250,
                "num_total_meetings": 22,
                "num_recurring_meetings": 16,
                "percent_good_use": 17.234
            },
            {
                "meeting_hours": 150,
                "company_time_dollars": 22050,
                "num_total_meetings": 20,
                "num_recurring_meetings": 15,
                "percent_good_use": 30.234
            },
            {
                "meeting_hours": 120,
                "company_time_dollars": 19250,
                "num_total_meetings": 23,
                "num_recurring_meetings": 17,
                "percent_good_use": 31.234
            }
        ]
    }
}'''