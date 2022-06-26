## Notes

    ./manage.py migrate
    ./manage.py loaddata gbi/sample

http://localhost:8000/graphql/


    fragment iconSource on IconObject {
        ... on Advisor { avatar }
        ... on Investor { avatar }
        ... on Plan { category { icon } }
    }

    query {
        notifications {
            id
            body
            icon1Object {
              __typename
              ...iconSource
            }
            icon2Object {
              __typename
              ...iconSource
            }
    	}
    }
