import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from "react-router-dom";
import NewNote from './components/NewNoteContainer';
import Login from './components/LoginContainer';
import MDSearch from './components/MDSearchContainer';
import HomeContainer from './components/HomeContainer';
import {BloodWorkForm, ImagingForm, ECGForm} from './components/RequisitionFormContainer';
import Prescription from './components/PrescriptionContainer';

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
                <Route path="/" exact component={HomeContainer} />
                {/* <Route path="/logout" component={Logout} /> */}
                <Route path="/newnote" component={NewNote} />
                <Route path="/login" component={Login}></Route>
                <Route path="/MDsearch" component={MDSearch}></Route>
                <Route path="/reqform/bloodwork" component={BloodWorkForm}></Route>
                <Route path="/reqform/imaging" component={ImagingForm}></Route>
                <Route path="/reqform/ecg" component={ECGForm}></Route>
                <Route path="/prescription" component={Prescription}></Route>
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
