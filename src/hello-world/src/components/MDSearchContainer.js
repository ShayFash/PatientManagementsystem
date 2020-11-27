import React, {useState} from 'react';
import NavBar from './NavBar';
import Demographics from './Demographics'

function MDSearch(props) {
    const [specialtySelected, setSpecialtySelected] = useState(false);
    if (!specialtySelected) {
        return <SpecialtyList isSelected={specialtySelected} setSpecialtySelected={setSpecialtySelected}/>
    }
    else {
        return <DoctorList />
    }
}

function SpecialtyList(props) {
    const [specialty, setSpecialty] = useState('');

    function changeSpecialty(event) {
        const {value} = event.target;
        setSpecialty(value);
    }

    return (
        <div className="homeContainer">
            <Demographics />
            <NavBar />
            <br />
            <form style={{height: "200px"}}>
                <select value={specialty} className="navBarButton" onChange={changeSpecialty}
                style={{border: "1px solid black"}}>
                    <option>-- Select Specialty --</option>
                    <option>Cardiac</option>
                    <option>Endocrinologist</option>
                    <option>Oncology</option>
                    <option>Orthopedics</option>
                    <option>Urology</option>
                </select>
                <br /><br />
                <button className="navBarButton" onClick={props.setSpecialtySelected}>Search</button>
            </form>
        </div>
    )
}

function DoctorList() {
    const [doctor, setDoctor] = useState('');

    function changeDoctor(event) {
        const {value} = event.target;
        setDoctor(value);
    }
    return (
        <div className="homeContainer">
            <Demographics />
            <NavBar />
            <br />
            <form style={{height: "200px"}}>
                <select className="navBarButton" value={doctor} onChange={changeDoctor}
                style={{border: "1px solid black"}}>
                    <option>-- Choose Doctor --</option>
                    <option>Dr. X</option>
                    <option>Dr. Y</option>
                    <option>Dr. Z</option>
                    <option>Dr. $</option>
                    <option>Dr. :)</option>
                </select>
                <br /><br />
                <button className="navBarButton">Search</button>
            </form>
        </div>
    )
}

export default MDSearch;