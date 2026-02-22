import { useEffect, useState } from "react";
import axios from "axios";
function App() {
  const [events, setEvents]=useState([]);
  const fetchEvents=async()=>{
    try{
      const res=await axios.get("http://localhost:5000/events");
      setEvents(res.data);
    }
    catch(error){
      console.error("Error fetching events:", error);
    }
  };

  useEffect(()=>{
    fetchEvents();
    const interval=setInterval(()=>{
      fetchEvents();
    },15000);
    return()=>clearInterval(interval);
  },[]);
  const renderMessage = (event)=>{
    if(event.action==="PUSH"){
      return `${event.author} pushed to ${event.to_branch} on ${event.timestamp}`;
    }
    if(event.action==="PULL_REQUEST"){
      return `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${event.timestamp}`;
    }
    if(event.action==="MERGE"){
      return `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${event.timestamp}`;
    }
    return "";
  };
  return(
    <div style={{padding:"40px", fontFamily:"Arial"}}>
      <h2>GitHub Activity</h2>
      {events.map((event, index)=>(
        <p key={index}>{renderMessage(event)}</p>
      ))}
      </div>
  );
}

export default App;