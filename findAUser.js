//the complexity of this program in o(n) 
const allStudents = ["a", "b", "c", "d", "e"];

const findStudent = (allStudent, studentName) => {
  for (let i = 0; i < allStudent.length; i++) {
    if (allStudent[i] === studentName) {
      console.log(`Found ${studentName}`);
      return;
    }
  }

  console.log(`${studentName} was not found on the array`);
};

findStudent(allStudents, "a");
