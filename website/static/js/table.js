const filterInput = document.querySelector(".filter-input");
      const tableRows = document.querySelectorAll("table tbody tr");

      filterInput.addEventListener("keyup", function () {
        const filterValue = filterInput.value.toLowerCase();
        for (let i = 0; i < tableRows.length; i++) {
          const name = tableRows[i]
            .querySelector("td:nth-child(1)")
            .textContent.toLowerCase();
          const rollno = tableRows[i]
            .querySelector("td:nth-child(2)")
            .textContent.toLowerCase();
          const department = tableRows[i]
            .querySelector("td:nth-child(3)")
            .textContent.toLowerCase();
          const ieee_member = tableRows[i]
            .querySelector("td:nth-child(4)")
            .textContent.toLowerCase();
          const member_id = tableRows[i]
            .querySelector("td:nth-child(5)")
            .textContent.toLowerCase();
          const email = tableRows[i]
            .querySelector("td:nth-child(6)")
            .textContent.toLowerCase();
          const event_name = tableRows[i]
            .querySelector("td:nth-child(7)")
            .textContent.toLowerCase();
          const team_name = tableRows[i]
            .querySelector("td:nth-child(8)")
            .textContent.toLowerCase();
          const team_members = tableRows[i]
            .querySelector("td:nth-child(9)")
            .textContent.toLowerCase();
          if (
            name.includes(filterValue) ||
            rollno.includes(filterValue) ||
            department.includes(filterValue) ||
            ieee_member.includes(filterValue) ||
            member_id.includes(filterValue) ||
            email.includes(filterValue) ||
            event_name.includes(filterValue) ||
            team_name.includes(filterValue) ||
            team_members.includes(filterValue)
          ) {
            tableRows[i].style.display = "";
          } else {
            tableRows[i].style.display = "none";
          }
        }
      });
      const event1 = document.querySelector("#filter-input");
      event1.addEventListener("input", function () {
        const event2 = document.getElementById("filter-input").value;
        event2.toLowerCase();
        for (let i = 0; i < tableRows.length; i++) {
          const event_name = tableRows[i]
            .querySelector("td:nth-child(7)")
            .textContent.toLowerCase();

          if (event_name.includes(event2)) {
            tableRows[i].style.display = "";
          } else {
            tableRows[i].style.display = "none";
          }
        }
      });

      const ieee = document.querySelector(".ieee");

      ieee.addEventListener("input", function () {
        var ieee_mem = document.getElementById("ieee").value;
        console.log(ieee_mem);

        ieee_mem.toLowerCase();
        for (let i = 0; i < tableRows.length; i++) {
          const ieee_member = tableRows[i]
            .querySelector("td:nth-child(4)")
            .textContent.toLowerCase();
          if (ieee_member.includes(ieee_mem)) {
            tableRows[i].style.display = "";
          } else {
            tableRows[i].style.display = "none";
          }
        }
      });
