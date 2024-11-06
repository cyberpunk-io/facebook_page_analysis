import requests
import pandas as pd

# Set your access token and page ID
access_token = input('YOUR ACCESS TOKEN')
page_id = input('YOUR PAGE ID')


# Function to get page posts
def get_facebook_page_posts(page_id, access_token):
    base_url = f'https://graph.facebook.com/v14.0/{page_id}/posts'
    fields = 'id,message,created_time,likes.summary(true),comments.summary(true)'
    url = f'{base_url}?fields={fields}&access_token={access_token}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f'Error: {response.status_code}')
        return None


# Fetch posts
posts = get_facebook_page_posts(page_id, access_token)

# Process and analyze the data
if posts:
    data = []
    for post in posts:
        post_id = post.get('id')
        message = post.get('message', '')
        created_time = post.get('created_time')
        likes = post.get('likes', {}).get('summary', {}).get('total_count', 0)
        comments = post.get('comments', {}).get('summary', {}).get('total_count', 0)
        shares = post.get('shares', {}).get('count', 0)
        reach = post.get('insights', {}).get('data', [{}])[0].get('values', [{}])[0].get('value', 0)
        impressions = post.get('insights', {}).get('data', [{}])[1].get('values', [{}])[0].get('value', 0)

        data.append({
            'Post ID': post_id,
            'Message': message,
            'Created Time': created_time,
            'Likes': likes,
            'Comments': comments,
            'Shares': shares,
            'Reach': reach,
            'Impressions': impressions
        })

    # Create a DataFrame
    df = pd.DataFrame(data)
    print(df.head())

    # Analyze the data (e.g., average likes and comments per post)
    avg_likes = df['Likes'].mean()
    avg_comments = df['Comments'].mean()
    print(f'Average Likes per Post: {avg_likes}')
    print(f'Average Comments per Post: {avg_comments}')








