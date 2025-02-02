import React from 'react';
import SearchBar from './SearchBar';
// from components to src, to apis, to youtube
import youtube from '../apis/youtube';
import VideoList from './VideoList';
import VideoDetail from './VideoDetail';

class App extends React.Component {

	state = {videos: [], selectedVideo: null};

// when the app first loads, show a default search term
	componentDidMount(){
		this.onTermSubmit('one bite pizza reviews');
	}

// retrieving list of video items
	onTermSubmit = async term => {
		console.log(term);
		const response = await youtube.get('/search', {
			params: {
				q: term
			}
		});
		this.setState({
			videos: response.data.items,
			selectedVideo: response.data.items[0]
		});
	};

	onVideoSelect = video => {
		this.setState({selectedVideo: video});
	};

	render(){
		return (
			<div className="ui container">
				<SearchBar callMeWhenSubmitted={this.onTermSubmit}/>
				<div className="ui grid">
					<div className="ui row">
						<div className="eleven wide column">
							<VideoDetail video={this.state.selectedVideo}/>
						</div>
						<div className="five wide column">
							<VideoList 
								onVideoSelect={this.onVideoSelect} 
								videos={this.state.videos}
							/>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

export default App;