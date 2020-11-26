import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";
import NewNote from './components/NewNote';
import Login from './components/Login';
import MDSearch from './components/MDSearch';
import NavBar from './components/NavBar';

class HomeContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render(){
        return (
            <div className="homeContainer">
                <h1>Hello, Dr. X</h1>
                <NavBar />
                <Demographics />
            </div>
        );
    }
}

class Demographics extends React.Component {
    render() {
        return (
            <div className="demographics">
                {/* I believe we're getting rid of
                    height, weight and family physician */}
                <p>Name:</p>
                <p>Address:</p>
                <p>DOB:</p>
                <p>Allergies:</p>
                <p>Family History:</p>
                <p>Medical Condition:</p>
                <p>Age:</p>
                <p>Height:</p>
                <p>Weight:</p>
                <p>Medications:</p>
                <p>Family Physician:</p>
            </div>
        );
    }
}

// class Logout extends React.Component {
//     render() {
//         /* Temporary obviously */
//         return <h1>Logged Out!</h1>
//     }
// }

export default function App() {
    return (
        <Router>
            <Switch>
                {/* <Route path="/" exact component={Login} /> */}
                <Route path="/" exact component={HomeContainer} />
                {/* <Route path="/logout" component={Logout} /> */}
                <Route path="/newnote" component={NewNote} />
                <Route path="/login" component={Login}></Route>
                <Route path="/MDsearch" component={MDSearch}></Route>
            </Switch>
        </Router>
    );
}

ReactDOM.render(
    <Router>
        <App />
    </Router>,
    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
