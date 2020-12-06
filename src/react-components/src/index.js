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
import PatientSearch from './components/PatientSearchContainer';
import ErrorMessage from './components/ErrorMessageContainer';

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
                <Route path="/" exact component={Login} />
                {/* <Route path="/logout" component={Logout} /> */}
                <Route path="/patient/:num/newnote" exact component={NewNote} />
                <Route path="/patient/" exact component={ErrorMessage}></Route>
                <Route path="/patient/:num" exact component={HomeContainer}></Route>
                <Route path="/patient/:num/MDsearch" exact component={MDSearch}></Route>
                <Route path="/patient/:num/reqform/bloodwork" exact component={BloodWorkForm}></Route>
                <Route path="/patient/:num/reqform/imaging" exact component={ImagingForm}></Route>
                <Route path="/patient/:num/reqform/ecg" exact component={ECGForm}></Route>
                <Route path="/patient/:num/prescription" exact component={Prescription}></Route>
                <Route path="/patientsearch" exact component={PatientSearch}></Route>
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
