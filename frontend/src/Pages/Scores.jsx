import React from 'react';
import './Style.css';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

const fetchData = async () => {
  const users = await prisma.user.findMany();
  console.log(users);
};

function Scores() {
    return <div className="scores">
            <h1>Scores</h1>
            </div>;
  }
  
export default Scores;