      implicit none

      integer*8 peixos(0:8), peixos0(0:8) 
      integer*8 i,dia,count

      peixos(0)=0
      peixos(1)=57
      peixos(2)=70      
      peixos(3)=58
      peixos(4)=48
      peixos(5)=67
      peixos(6)=0
      peixos(7)=0
      peixos(8)=0

      do dia=1,256
            do i=0,8
                  peixos0(i)=peixos(i)
            enddo
            do i=0,7
                  peixos(i)=peixos0(i+1)
            enddo
            peixos(6)=peixos(6)+peixos0(0)
            peixos(8)=peixos0(0)
      enddo


      count=0
      do i=0,8
            count=count+peixos(i)
      enddo
      print*, count

      end