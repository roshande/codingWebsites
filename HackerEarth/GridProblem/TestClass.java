import java.io.*;
import java.util.*;

class TestClass {
	public static void main(String args[] ) throws Exception {
		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();
		for(int i=0;i<T;++i)
		{
			int N=scanner.nextInt();
			int[][] matrix = new int[N][N];
			for(int j=0;j<N;++j)
			{
				for(int k=0;k<N;++k)
				{
					matrix[j][k]=scanner.nextInt();
				}
			}
			
			Hashtable<String,Integer> table = new Hashtable<String,Integer>();
			for(int j=0;j<N;++j)
			{
				for(int k=0;k<N;++k)
				{
					String key = String.format("%d,%d,%d,%d",j,k,j,k);
					//String key = new String(Integer(j).toString()+","+Integer(k).toString()+","+Integer(j).toString()+","+Integer(k).toString());
					table.put(key,matrix[j][k]);
				}
			}
			//System.out.println(table.size());
			for(int p=0;p<N;++p)
			{
				for(int q=0;q<N;++q)
				{
					for(int r=0;(p+r+1)<N && (q+r+1)<N;++r)
					{
						String key = String.format("%d,%d,%d,%d",p,q,p+r,q+r);
						//String key = new String(Integer(p).toString()+","+Integer(q).toString()+","+Integer(p+r).toString()+","+Integer(q+r).toString());
						if(table.get(key)!=null)
						{
							//int value = table.get(key);
							int value = matrix[p][q];
							boolean flag=true;
							if(matrix[p+r+1][q+r+1]!=value)
								flag=false;
							for(int s=1;flag && s<=r+1 && (p+r+s)<N && (q+r+s)<N;++s)
							{
								if(matrix[p+r+s][q]!=value || matrix[p][q+r+s]!=value)
								{
									flag=false;
									break;
								}
							}
							if(flag)
							{
								key = String.format("%d,%d,%d,%d",p,q,p+r+1,q+r+1);
								table.put(key,matrix[p][q]);
							}
						}
						else
						{
							break;
						}
					}
				}
			}
			System.out.println(table.size());
			table.clear();
		}
	}
}

