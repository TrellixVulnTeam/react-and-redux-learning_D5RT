import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

import App from './components/App';
import reducers from './reducers';

if (module.hot) {
	module.hot.accept();
  }

  // hooking up middleware to the redux store
const store = createStore(reducers, applyMiddleware(thunk));

ReactDOM.render(
	// middleware and reducers passed in here
	<Provider store={store}>
	<App />
	</Provider>,
	document.querySelector('#root')
);