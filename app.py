from flask import Flask, jsonify, request

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]


def binary_search(arr, target): # O(log n)
    low = 0 # Beginning index
    high = len(arr) - 1 # Ending Index

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif mid < arr.index(target):
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Merge Sort:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result.extend(left_half[i:])

    result.extend(right_half[j:])

    return result
      

@app.route('/sort')
def sort_titles():
    sorted_titles = merge_sort(video_titles)
    return jsonify({'Sorted Titles': sorted_titles})

    
@app.route('/search', methods=['GET'])
def search_video():
    title_query = request.args.get('title')
    if not title_query:
        return "Please provide a search query."

    index = binary_search(video_titles, title_query)
    
    if index != -1:
        return jsonify({"title": video_titles[index], "index": index}), 200
    else:
        return jsonify({"message": "Video not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)

